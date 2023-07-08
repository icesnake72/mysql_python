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

    if ( document.getElementById("clock")!=null )
        document.getElementById("clock").innerHTML = time;
}

function todoDelete(id)
{
    console.log("삭제")

    var url = "http://172.30.1.71:5001/delete_todo";
    var data = {'todo_id':id };
    fetchUrl(url, data)   
}

function checkBoxClick(event, id, user_id)
{
    // event.preventDefault(); // 폼의 기본 동작인 페이지 이동을 막음
    // console.log(event.target.checked);
    console.log("checkbox click");

    var url = "http://172.30.1.71:5001/update_done";
    var data = {'todo_id':id, 'user_id': user_id, 'done':event.target.checked };
    fetchUrl(url, data)

    // console.log(data);
    // console.log(`${data.todo_id}`)    
}


function fetchUrl(url, data)
{
    fetch(url, 
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        }
    )
    .then(function(response) {
        if (response.ok) {
            console.log("요청이 성공적으로 완료되었습니다.");
            // 추가적인 동작을 수행할 수 있습니다.
            if ( response.redirected )
                window.location.href = response.url;

        } else {
          console.log("요청이 실패하였습니다.", response.status);
        }
    })
    .catch(function(error) {
        console.log("요청 중에 오류가 발생하였습니다.", error);
    });        
}