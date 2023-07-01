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

function checkBoxClick(id, user_id)
{
    var url = "http://127.0.0.1:5001/";
    var data = {todo_id:id, user_id:user_id};

    console.log(data);

    // XMLHttpRequest 객체 생성
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // 요청 보내기
    xhr.send(JSON.stringify(data));
}