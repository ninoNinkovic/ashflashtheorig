// This script ensures the height of the page fits as it is intended to.
// It tries to be as responsive as it can. It was my first attempt at building
// a responsive site with an unconventional design layout.


$(document).ready(function() {
    $('.image > img').each(function() {
        $(this).click(function() {
            var src = $(this).attr("src").replace('_thumb.jpg', '.jpg');
            $.modal('<img src="' + src + '"width=800">');
        });
    });
    
    $('#music_block > iframe').css('width', $('#right_side').width() - 33);
});

$(window).resize(function() {
    $('#music_block > iframe').css('width', $('#right_side').width() - 33);
});

		$('#music_heading').click(function() {
		    var vid = $('#video_block').css('display');
		    var pics = $('#picture_block').css('display');
		    
						$('#music_block').slideToggle('slow');
						if( vid == 'block') {
						    $('#video_block').slideToggle('slow');
						}
						if( pics == 'block' ) {
						    $('#picture_block').slideToggle('slow');
						}
		});
		
		$('#video_heading').click(function() {
		    var music = $('#music_block').css('display');
		    var pics = $('#picture_block').css('display');
						
						$('#video_block').slideToggle('slow');
						if( music == 'block' ) {
						    $('#music_block').slideToggle('slow');
						}
						if( pics == 'block' ) {
						    $('#picture_block').slideToggle('slow');
						}
		});

		$('#picture_heading').click(function() {
		    var vid = $('#video_block').css('display');
		    var music = $('#music_block').css('display');
		    
						$('#picture_block').slideToggle('slow');
						if( vid == 'block' ) {
						    $('#video_block').slideToggle('slow');
						}
						if( music == 'block' ) {
						    $('#music_block').slideToggle('slow');
						}
		});