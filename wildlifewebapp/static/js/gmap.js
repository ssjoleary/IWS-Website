/**
 * Created by ssjoleary on 26/02/14.
 */

$(function(){
    var mapOptions
    var map
    var centerLatLng

    mapOptions = {
        center: new google.maps.LatLng(53.41608, -7.93396),
        zoom: 6
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    //attach a jQuery live event to the button
    $(document).ready( function(){

        $.getJSON("/sightings/getsighting", function( data ) {

            centerLatLng = new google.maps.LatLng(53.41608,-7.93396)

            $.each(data, function(index, element){
                var sightingLatLng = new google.maps.LatLng(element.fields.latitude, element.fields.longitude)
                // To add the marker to the map, use the 'map' property
                var marker = new google.maps.Marker({
                    position: sightingLatLng,
                    map: map,
                    title: element.fields.location,
                    animation: google.maps.Animation.DROP
                });
                var contentString = '<h1><small>'+element.fields.sub_date+'</small></h1>' +
                    '<h2><small>Species:</small></h2><p>'+element.fields.species+'</p>'+
                    '<h2><small>Animals:</small></h2><p>'+element.fields.animals+'</p>'+
                    '<h2><small>Location:</small></h2><p>'+element.fields.location+'</p>'+
                    '<h2><small>Latitude:</small></h2><p>'+element.fields.latitude+'</p>'+
                    '<h2><small>Longitude:</small></h2><p>'+element.fields.longitude+'</p>';

                var infowindow = new google.maps.InfoWindow({
                    content: contentString
                });
                google.maps.event.addListener(marker, 'click', function() {

                    infowindow.open(map,marker);
                });
                google.maps.event.addListener(infowindow, 'closeclick', function() {
                    infowindow.close(map,marker)
                    map.panTo(centerLatLng)
                    map.setZoom(6)
                })

            });
            $.each(data, function(index, element) {
                var $tableData = $('<tr>').append(
                    $('<td>').text(element.fields.sub_date),
                    $('<td>').text(element.fields.species),
                    $('<td>').text(element.fields.animals),
                    $('<td>').text(element.fields.location),
                    $('<td>').text(+element.fields.latitude),
                    $('<td>').text(element.fields.longitude)
                ).appendTo('#sightingsTablebody')
            });

        });
    });

    $('#addSightingbtn').on('click', function() {
        $('#myModal').modal('show')
    });
});
