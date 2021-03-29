let  theme = localStorage.getItem('theme')

if (theme == null){
    SetTheme('light')

}else{
    SetTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for( var i=0; themeDots.length > i; i++){
    themeDots[i].addEventListener('click', function(){
        let mode = this.dataset.mode

        console.log('options ', mode)

        SetTheme(mode)
    })

}


function SetTheme(mode){
    if(mode == 'light'){
        document.getElementById('theme-style').href =  static + '/default.css'
    }

    if(mode == 'blue'){
        document.getElementById('theme-style').href = static + '/blue.css'
    }

    if(mode == 'green'){
        document.getElementById('theme-style').href = static + '/green.css'
    }

    if(mode == 'purple'){
        document.getElementById('theme-style').href = static + '/purple.css'
    }

    localStorage.setItem('theme', mode)


}
