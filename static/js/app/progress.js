const progress = document.querySelector('.detail .progress-done')

let now = progress.getAttribute('data-done')
let max = progress.getAttribute('data-max')
var calculated = (max, now) => {
    let percent = (now - 0) * (100 - 0) / (max - 0) + 0
    if (percent >= 100)
        progress.style.width = '100%'
    else if (percent >= 0)
        progress.style.width = `${parseInt(percent)}%`
}


setTimeout(() => {
    if (now != 0)
        calculated(max, now)
    else
        progress.style.width = `0%`
    progress.style.opacity = 1
}, 500)