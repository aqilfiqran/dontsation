window.onload = () => {
    const btn_top_donate = document.querySelectorAll('.capacity .top-donate')

    btn_top_donate.forEach(btn => {
        btn.addEventListener('click', (res) => {
            document.querySelector('.capacity .top-donate.selected').classList.remove('selected')
            res.target.classList.add('selected')
        })
    })

}