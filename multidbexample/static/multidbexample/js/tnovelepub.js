/**
 * Created by skuppusw on 8/19/2016.
 */

function get_id_html(id, url_link, form_data) {
    $.ajax({
            type: 'GET',
            url: url_link,
            data: form_data,
            success: function (data, textStatus) {
                $(id).html(data)
            },
            error: function(xhr, status, e) {
                alert(status);
                $(id).html('<p>An error has occurred</p>');
                return e;
            }
    });
}

function form_post_data(id, url_link, form_data) {
    $.ajax({
        type: 'POST',
        url: url_link,
        data: form_data,
        success: function (data, textStatus) {
            return textStatus;
        },
        error: function (xhr, status, e) {
            alert(status);
            return e;
        }
    });
}