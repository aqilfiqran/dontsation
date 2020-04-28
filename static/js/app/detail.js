window.onload = () => {
    const btn_top_donate = document.querySelectorAll('.capacity .top-donate')
    const btn_colours = document.querySelectorAll('.colours .colour')

    btn_top_donate.forEach(btn => {
        btn.addEventListener('click', (res) => {
            document.querySelector('.capacity .top-donate.selected').classList.remove('selected')
            res.target.classList.add('selected')
        })
    })

    btn_colours.forEach(btn => {
        btn.addEventListener('click', res => {
            document.querySelector('.colours .colour.selected').classList.remove('selected')
            res.target.classList.add('selected')
        })
    })
}