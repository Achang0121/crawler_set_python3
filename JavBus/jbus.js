var gid = 45864909470;
var uc = 0;
var img = 'https://pics.javbus.com/cover/853n_b.jpg';


$(function () {
    var t = "https://pics.javbus.com/ajax/uncledatoolsbyajax.php?gid=" + gid + "&lang=" + lang + "&img=" + img + "&uc=" + uc + "&floor=" + Math.floor(1e3 * Math.random() + 1);
    $.ajax({
        url: t,
        type: "GET",
        success: function (t) {
            return t
        }
    })
});

