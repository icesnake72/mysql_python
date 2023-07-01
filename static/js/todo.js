// var updateButton = document.getElementById("Todo_Update");
// var deleteButton = document.getElementById("Todo_Delete");

// updateButton.addEventListener("click", todoUpdate);
// deleteButton.addEventListener("click", todoDelete);
setInterval(displayTime, 1000);

function displayTime() 
{
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth();
    var day = date.getDay();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    var time = year + "년 " + month + "월 " + day + "일, " + hours + "시 " + minutes + "분 " + seconds + "초";

    document.getElementById("clock").innerHTML = time;
}

function todoUpdate()
{
    console.log("수정")
}

function todoDelete()
{
    console.log("삭제")
}