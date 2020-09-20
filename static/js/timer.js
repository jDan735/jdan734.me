var starts = moment('2020-06-18 01:38:41')

function timer(){
    var ends = moment()

    times = [
        ends.diff(starts, "days"),
        ends.diff(starts, "weeks"),
        ends.diff(starts, "month"),
        ends.diff(starts, "minutes"),
        ends.diff(starts, "seconds")
    ]

    $time_text = `${times[0]} дней, ${times[1]} недель, ${times[2]} месяцев`
    $time2_text = `${times[3]} минут, ${times[4]} секунд`

    $(".time").text($time_text)
    $(".time2").text($time2_text)
    console.log($time_text)

}


$(() => {
    timer()
    window.setInterval(timer, 60)
})

