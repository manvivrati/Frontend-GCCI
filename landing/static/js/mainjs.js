// Partners slider
$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});


//Counter
$(document).ready(function() {
    $('.counter').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
});


// Achievements charts
$(document).ready(function() {
    var ctx = $("#chart-line1");
    var myLineChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["Special Award", "CONST. in Excellence Award", "Excellence CAT.A Award"],
            datasets: [{
                data: [1, 9, 14],
                backgroundColor: ["rgba(255, 0, 0, 0.5)", "rgba(200, 50, 255, 0.5)", "rgba(100, 255, 0, 0.5)"]
            }]
        },
        options: {
            title: {
                display: true,
                text: 'GCCI'
            },
            legend: {
                position: "right",
                align: "middle"
            },
        }
    });
});

$(document).ready(function() {
    var ctx = $("#chart-line2");
    var myLineChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["CONST. in Excellence Award", "Excellence CAT.B Award", "Excellence CAT.A Award"],
            datasets: [{
                data: [2, 3, 16],
                backgroundColor: ["rgba(255, 0, 0, 0.5)", "rgba(100, 255, 0, 0.5)", "rgba(200, 50, 255, 0.5)"]
            }]
        },
        options: {
            title: {
                display: true,
                text: 'GCCI'
            }
        }
    });
});

$(document).ready(function() {
    var ctx = $("#chart-line3");
    var myLineChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["Special Award", "Excellence CAT.A Award", "CONST. in EXCELLENCE AWARD"],
            datasets: [{
                data: [10, 8, 15],
                backgroundColor: ["rgba(255, 0, 0, 0.5)", "rgba(100, 255, 0, 0.5)", "rgba(200, 50, 255, 0.5)"]
            }]
        },
        options: {
            title: {
                display: true,
                text: 'GCCI'
            }
        }
    });
});


// Testimonials
(function () {
    "use strict";

    var carousels = function () {
    $(".owl-carousel1").owlCarousel({
        loop: true,
        center: true,
        margin: 0,
        responsiveClass: true,
        nav: false,
        responsive: {
        0: {
            items: 1,
            nav: false
        },
        680: {
            items: 2,
            nav: false,
            loop: false
        },
        1000: {
            items: 3,
            nav: true
        }
        }
    });
    };

    (function ($) {
        carousels();
    })(jQuery);
})();

// Profile
$(function(){
    $("#fileupload").change(function(event) {
        var x = URL.createObjectURL(event.target.files[0]);
        $("#upload-img").attr("src",x);
        console.log(event);
    });
})

