/* Add dates and special events to the syllabus. */

(function() {

    //////////////
    // Schedule //
    //////////////

    // REMINDER: Months are 0-indexed in Javascript Dates
    var firstLecture = new Date(2016, 0, 20);
    var noLecture = [
        new Date(2016, 1, 15),  // Holiday
        new Date(2016, 2, 21),  // Spring break
        new Date(2016, 2, 23),  // Spring break
        new Date(2016, 2, 25),  // Spring break
        new Date(2016, 2, 14),  // Midterm review
        new Date(2016, 2, 16),  // Midterm
    ];
    noLecture = $.map(noLecture, function(d) { return d.toDateString() });

    // Date of lecture n
    function getLectureDate(n) {
        var next = firstLecture;
        for (var i = 0; i < n; i++) {
            var days = (next.getDay() == 5) ? 3 : 2;
            next = new Date(next.getFullYear(), next.getMonth(), next.getDate() + days);
            if ($.inArray(next.toDateString(), noLecture) > -1) i--;  // Skip
        }
        return next;
    }

    var addDates = function() {
        $("#gcb-nav-y>ul>ul>li>p>:nth-child(1)").after(function(i) {
            return "<span class=\"lecture-date\">" + getLectureDate(i).toDateString().slice(0, -5) + "</span>";
        });
    }

    var findLectures = function() {
        var lectures = {};
        $("#gcb-nav-y>ul>ul>li>p>:nth-child(3)").foreach(function(i) {
            dateCells[getLectureDate(i)] = this;
        });
        return lectures;
    }

    ///////////
    // Links //
    ///////////

    var lab = function(number, date) {
        return {
            name: "Lab " + number,
            link: "https://data8.berkeley.edu/hub/interact?repo=data8assets&path=labs/lab" + number,
            date: date
        }

    var labs = [
        lab("01", new Date(2016, 1, 20)),
        lab("02", new Date(2016, 1, 27))
    ]
    var homeworks = []
    var projects = []

    links = labs.concat(homeworks).concat(projects)

    var addLinks = function(lectures) {
        // TODO add links to cells by date
    }

    $(document).ready(function () {
        addDates();
        lectures = findLectures();
        console.log(lectures);
        addLinks(lectures)
    });
})();
