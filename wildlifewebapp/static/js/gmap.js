/**
 * Created by ssjoleary on 26/02/14.
 */

$(function($,W,D,undefined)
{
    var mapOptions
    var map
    var centerLatLng
    var markers = [];

    GMAP = {
        name: "Gmap Sightings",
        namespace: "GMAP",
        settings: {

        },
        cache: {

        },

        init: function(){
            mapOptions = {
                center: new google.maps.LatLng(53.41608, -7.93396),
                zoom: 7
            };
            map = new google.maps.Map(document.getElementById("map-canvas"),
                mapOptions);
            //attach a jQuery live event to the button


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
                        '<h2><small>Longitude:</small></h2><p>'+element.fields.longitude+'</p>'+
                        '<h2><small>Observer:</small></h2><p>'+element.fields.name+'</p>'+
                        '<h2><small>Image:</small></h2><a href="'+element.fields.image+'"><img src="'+element.fields.image+'.jpg'+'" title="Hosted by imgur.com" /></a>';

                    var infowindow = new google.maps.InfoWindow({
                        content: contentString
                    });
                    google.maps.event.addListener(marker, 'click', function() {

                        infowindow.open(map,marker);
                    });
                    google.maps.event.addListener(infowindow, 'closeclick', function() {
                        infowindow.close(map,marker)
                        map.panTo(centerLatLng)
                        map.setZoom(7)
                    });
                    markers.push(marker)
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
                /*$.each(data, function(index, element) {
                 var $dropdownData = $('<li>').append(
                 $('<a href="#">').text(element.fields.species)
                 ).append('</a></li>'
                 ).appendTo('#dropdownSpeciesSearch')
                 });*/

            });
            this.setupEventHandlers();
        },

        setupEventHandlers: function(){
            var _this = this;

            $('#addSightingbtn').on('click', function()
            {
                $('#myModal').modal('show')
            });

            $(".dropdown-menu li a").on('click', function()
            {
                var selText = $(this).text();
                $(this).parents('.dropdown').find('.dropdown-toggle').html(selText+'<span class="caret"></span>');
            });


            $('#pictureInput').on('change', function(e)
            {
                e.preventDefault();
                console.log('getting image...');
                _this.uploadImage();
            });

            $('#searchbtn').on('click', function()
            {
                var countySearch = $('#dropdownCountyInput').text().trim();
                var speciesSearch = $('#dropdownSpeciesInput').text().trim();
                var search = { county: countySearch, species: speciesSearch };
                $.ajax({
                    url: '/sightings/getspecificsighting/',
                    type: 'POST',
                    contentType: 'application/json; charset=utf-8',
                    data: JSON.stringify(search),
                    dataType: 'json',
                    success: function(data)
                    {
                        if(data.length == 0) {
                            alert('No result matched your query!');
                            return;
                        }


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
                                '<h2><small>Longitude:</small></h2><p>'+element.fields.longitude+'</p>'+
                                '<h2><small>Observer:</small></h2><p>'+element.fields.name+'</p>'+
                                '<h2><small>Image:</small></h2><a href="'+element.fields.imageurl+'"><img src="'+element.fields.imageurl+'.jpg'+'" title="Hosted by imgur.com" /></a>';

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
                            });
                            markers.push(marker)
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
                    }

                });
            })

            function setAllMap(map) {
                for (var i = 0; i < markers.length; i++) {
                    markers[i].setMap(map);
                }
            }

            function clearMarkers() {
                setAllMap(null);
            }
        },

        uploadImage: function()
        {
            var _this = this,
                $imgInput = $('#pictureInput');

            $.ajaxFileUpload(
                {

                }
            )
        }
    }

    $(document).ready( function(){
        GMAP.init();
    });

});
