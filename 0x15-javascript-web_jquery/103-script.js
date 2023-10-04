$(document).ready(function() {
    
    function fetchTranslation() {
        const langCode = $('#language_code').val();
        
        $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keydown(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
