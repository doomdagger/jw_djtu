/**
 * Created by Li He on 2014/7/10.
 */

function jw_get(url, data) {
    var main = $('.main');

    NProgress.start();

    main.html('<div style="text-align: center; "><br><br><i class="fa fa-spinner fa-spin fa-3x"></i></div>');

    setTimeout(function () {
        $.get(url, data).
        done(function (page) {
            main.fadeOut(500, function () {
                main.html(page);
                main.fadeIn(300);
            });
        }).
        fail(function () {
            alert('Fail!');
        }).
        always(function () {
            NProgress.done();
        });
    },1500);

}

$('a[data-url]').click(function(event){
    event.preventDefault();

    jw_get($(this).attr('data-url'));

});