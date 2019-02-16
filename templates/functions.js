function props(newLat,newLng,newContent)
{
    this.coords = {lat: newLat, lng: newLng},
    this.information = newContent;
};
//Place object with lat and long
var result;
var markers = [];

function initMap(){
    var options = {
        zoom: 13,
        center: {lat:37.7749, lng: -122.4194},
        mapTypeControl: false,
        streetViewControl: false,
        fullscreenControl: false
    };
    //creating a new map
    //set up strict bounds for map to SF
    var map = new google.maps.Map(document.getElementById('map'), options);
    //Array

    //takes in props object
    function addMarker(props)
    {
        //delete any existing markers
        //zoom in on marker
        //console.log(props.coords);
        var marker = new google.maps.Marker({
        position: props.coords,
        map: map
        //used to set a custom icon
        //icon:
        });

        //check content
        if(props.content)
        {
            var infoWindow = new google.maps.InfoWindow({
            content: props.content
            });

            marker.addListener('click', function(){
            infoWindow.open(map, marker)});
        }

        markers.push(marker);

    };

    function deleteMarkers(map)
    {
        for(var i = 0; i < markers.length; ++i)
        {
            markers[i].setMap(map);
        }

    };

    function clearMarkers()
    {
        deleteMarkers(null);
    };
    // set SF boundaries;

    var SFboundaries;
    var input = document.getElementById('input');

    var field = new google.maps.places.Autocomplete(input);
    field.bindTo('bounds', map);
    field.setFields(['geometry', 'name']);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

    field.addListener("place_changed", function() {
        result = field.getPlace();
        if (!result.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        } else {
            clearMarkers();
            var p = new props(result.geometry.location.lat(), result.geometry.location.lng(), result.name);
            options.center = {lat: result.geometry.location.lat(), lng:result.geometry.location.lng()};

            options.zoom = 15;
            map.panTo(options.center);
            //map = new google.maps.Map(document.getElementById('map'), options);
            console.log(result);
            addMarker(p);
            //set up JSON for flask to handle
            var location = result.geometry.location.toJSON();
            console.log(location);
            //call Flask function - returns JSON
            $.ajax({
                url: "/results",
                type: "POST",
                data: JSON.stringify(location),
                success: function(data, textStatus, jqXHR) {
                },
                contentType: "application/json",
                dataType: "json"
            });
            input.value = "";
            var results = $.get("/results");
            console.log(results);
            //get multiple JSON strings
            //create markers for each
        }

        //TODO search for vehicle incidents - backend
        //TODO back end code
    });
}
