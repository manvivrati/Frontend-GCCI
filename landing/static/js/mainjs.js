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

// Achievements charts
$(document).ready(function(){
    var ctx = $("#firstcanvas").get(0).getContext("2d");
    var data = [
        {
            value: 14,
            color: "cornflowerblue",
            highlight: "lightskyblue",
            label: "JavaScript"
        },
        {
            value: 9,
            color: "lightgreen",
            highlight: "yellowgreen",
            label: "HTML"
        },
        {
            value: 1,
            color: "orange",
            highlight: "darkorange",
            label: "CSS"
        }
    ];
    var chart = new Chart(ctx).Doughnut(data);
});

$(document).ready(function(){
    var ctx = $("#secondcanvas").get(0).getContext("2d");
    var data = [
        {
            value: 16,
            color: "cornflowerblue",
            highlight: "lightskyblue",
            label: "JavaScript"
        },
        {
            value: 2,
            color: "lightgreen",
            highlight: "yellowgreen",
            label: "HTML"
        },
        {
            value: 3,
            color: "orange",
            highlight: "darkorange",
            label: "CSS"
        }
    ];
    var chart = new Chart(ctx).Doughnut(data);
});

$(document).ready(function(){
    var ctx = $("#thirdcanvas").get(0).getContext("2d");
    var data = [
        {
            value: 15,
            color: "cornflowerblue",
            highlight: "lightskyblue",
            label: "JavaScript"
        },
        {
            value: 10,
            color: "lightgreen",
            highlight: "yellowgreen",
            label: "HTML"
        },
        {
            value: 8,
            color: "orange",
            highlight: "darkorange",
            label: "CSS"
        }
    ];
    var chart = new Chart(ctx).Doughnut(data);
});