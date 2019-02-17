function props(newLat,newLng,newContent, iconURL)
{
    this.coords = {lat: newLat, lng: newLng},
    this.information = newContent;
    this.icon = iconURL
};
//Place object with lat and long
var markers = [];
var circle;
var map;
function changeCircle() {
    if (circle != null) {
        slider = document.getElementById("myRange");
        circle.setRadius(parseInt(slider.value));
        sendRequest(circle.getCenter());
    }
    //TODO change text box value
}

function updateInputBox(){
    var slider = document.getElementById("myRange")
    inputBoxSlider.value = parseInt(slider.value);
    slider.html = inputBoxSlider.value;
    //TODO change slider value and slider position as well
}

function sendRequest(l) {
    clearMarkers();
    var location = l.toJSON();
    location.radius = circle.getRadius();
    $.ajax({
        url: "/results",
        type: "POST",
        data: JSON.stringify(location),
        success: function(data, textStatus, jqXHR) {
        },
        contentType: "application/json",
        dataType: "json"
    });

     $.get("/results", function(data) {
        incidents = JSON.parse(data);

        for (var i in incidents) {
            console.log(i);
            p = new props(incidents[i].latitude, incidents[i].longitude, incidents[i].description, 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png');
            addMarker(p);
        }
    });
}
function addMarker(props)
{
    var marker = new google.maps.Marker({
    position: props.coords,
    map: map,
    //used to set a custom icon
    icon: props.icon
    });

    //check content
    if(props.information)
    {
        var infoWindow = new google.maps.InfoWindow({
        content: props.information
        });

        marker.addListener('mouseover', function(){
        infoWindow.open(map, marker)});

        marker.addListener('mouseout', function(){
            infoWindow.close();
        });

    }
    markers.push(marker);
    google.maps.event.addListener(infoWindow,'closeclick',function(){

    });
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

function initMap(){
    //remove clutter on map
    var mapStyles = [
        {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
        {
            featureType: 'poi',
            stylers: [{visibility: 'off'}]
        },
        {
            featureType: 'transit',
            stylers: [{visibility: "off"}]
        },

            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
    ];
    var options = {
        zoom: 13,
        center: {lat:37.7749, lng: -122.4194},
        mapTypeControl: false,
        streetViewControl: false,
        fullscreenControl: false,
        styles: mapStyles
    };
    //set up strict bounds for map to SF
    map = new google.maps.Map(document.getElementById('map'), options);
    // set SF boundaries;
    var SFboundaries;
    var input = document.getElementById('input');
    var inputBoxSlider = document.getElementById('input-for-slide');

    var slide = document.getElementById('slidecontainer');
    //set up autocomplete box
    var field = new google.maps.places.Autocomplete(input);
    field.bindTo('bounds', map);
    field.setFields(['geometry', 'name']);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(slide);

    document.getElementById("myRange").addEventListener("mouseup", updateInputBox);

    //main area of functionality
    document.getElementById("myRange").addEventListener("mouseup", changeCircle);
    field.addListener("place_changed", function() {
        var result = field.getPlace();
        if (!result.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        } else {
            var p = new props(result.geometry.location.lat(), result.geometry.location.lng(), result.name);
            
            options.center = {lat: result.geometry.location.lat(), lng:result.geometry.location.lng()};

            map.setZoom(16);
            map.panTo(options.center);
            //map = new google.maps.Map(document.getElementById('map'), options);
            addMarker(p);
            input.value = "";

            //create circle at this location
            if (circle != null)
                circle.setCenter(p.coords);
            else
                circle = new google.maps.Circle(
                    {   center: p.coords,
                        strokeColor: '113F55',
                        strokeOpacity: 0.5,
                        strokeWeight: 1,
                        fillColor: '23576F',
                        editable: false,
                        draggable: false,
                        fillOpacity: 0.3,
                        map: map,
                        radius: 300
                    }
                );
            //populate circle with data
            sendRequest(circle.getCenter());
        }
    });
}
