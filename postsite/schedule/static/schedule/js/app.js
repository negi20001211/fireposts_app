document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      locale:'ja',  
      initialView: 'dayGridMonth',
      selectable: true,
      select: function (info) {
        const eventName = prompt("イベントを入力してください");
        
        if (eventName) {

            // 登録処理の呼び出し
            axios
                .post("/sc/add/", {
                    start_date: info.start.valueOf(),
                    end_date: info.end.valueOf(),
                    event_name: eventName,
                })
                .then(() => {
                    // イベントの追加
                    calendar.addEvent({
                        title: eventName,
                        start: info.start,
                        end: info.end,
                        allDay: true,
                    });

                })
                .catch(() => {
                    // バリデーションエラーなど
                    alert("登録に失敗しました");
                });
        }
    },
    

    });
    calendar.render();
  });