const progress = document.querySelector('.progress-bar')

let now = progress.getAttribute('aria-valuenow')
let max = progress.getAttribute('aria-valuemax')
var calculated = (max, now) => {
    let percent = (now - 0) * (100 - 0) / (max - 0) + 0
    if (percent >= 100)
        progress.style.width = '100%'
    else if (percent >= 0)
        progress.style.width = `${parseInt(percent)}%`
    progress.innerHTML = `${progress.style.width}`
}

if (now != 0)
    calculated(max, now)
else
    progress.style.width = `0%`