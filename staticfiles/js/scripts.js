$(document).ready(function() {

   
    var baseUrl = 'http://127.0.0.1:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter')

    $(deleteBtn).on('click', function(e) {

        e.preventDefault();
        
        var delLink = $(this).attr('href');
        var result = confirm(`Você tem certeza que deseja excluir essa tarefa?`);

        if(result) {
            window.location.href = delLink;
        }
    }); 

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });

    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    })


    let sidebar = document.querySelector(".box");
    let closeBtn = document.querySelector("#btn");
   
    

    let box = document.querySelector(".box");


    closeBtn.addEventListener("click", ()=>{
        box.classList.toggle("open");
        menuBtnChange();
    });

    function menuBtnChange() {
        if(box.classList.contains("open")){
            closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
        }else {
            closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
        }
    }






});