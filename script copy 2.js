        // Import the functions you need from the SDKs you need
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
        import { getDatabase, set, get, ref } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-database.js";

        // import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-analytics.js";
        // TODO: Add SDKs for Firebase products that you want to use
        // https://firebase.google.com/docs/web/setup#available-libraries
      
        // Your web app's Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
        const firebaseConfig = {
          apiKey: "AIzaSyCcetRJa_ybgnHTKfOfz4PU8XlSzh6f7i0",
          authDomain: "facerecognitionbasedatte-b4a54.firebaseapp.com",
          databaseURL: "https://facerecognitionbasedatte-b4a54-default-rtdb.firebaseio.com",
          projectId: "facerecognitionbasedatte-b4a54",
          storageBucket: "facerecognitionbasedatte-b4a54.appspot.com",
          messagingSenderId: "1011023746816",
          appId: "1:1011023746816:web:03a1da48a7d52cce58c5e5",
          measurementId: "G-RLQH0YNVRH"
        };
      
        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        // const analytics = getAnalytics(app);
        const db = getDatabase(app)
        // console.log(db)
        // console.log("good");
        // function readUserData(){
        //     const userRef = ref(db,'Students');

        //     get(userRef).then((Students)=>{
        //         Students.forEach(StdID => {
        //             console.log(StdID.val());
        //         })
        //     })
        // }
        // readUserData()
        function readUserData() {
            const userRef = ref(db, 'Students');
            var table = document.getElementById("main_table");
            const fDate = [];
        
            // to put Dates column in table
            for (var date = new Date("2024-03-29"); date <= new Date("2024-04-15"); date.setDate(date.getDate() + 1)) {
                var day = date.getDate();
                var month = date.getMonth() + 1; // Months are zero-based, so add 1
                var year = date.getFullYear();
        
                // Create a formatted date string
                var formattedDate = (day < 10 ? "0" + day : day) + ":" + (month < 10 ? "0" + month : month) + ":" + year ;
                fDate.push(formattedDate);
        
                var headerCell = document.createElement('th');
                headerCell.textContent = formattedDate;
                headerCell.colSpan = 3;
        
                var subHeaders = ['L 1', 'L 2', 'L 3'];
                for (let j = 0; j < 3; j++) {
                    var subHeader = document.createElement('th');
                    subHeader.textContent = subHeaders[j];
                    headerCell.appendChild(subHeader); // Append sub header to header cell
                }
                table.rows[0].appendChild(headerCell); // Append header cell to table row
            }
        
            get(userRef).then((Students)=>{
                var stdNo=0;
                Students.forEach((studentSnapshot) => {
                    const studentData = studentSnapshot.val();
                    const studentID = studentSnapshot.key;
                    const fname = studentData.fname;
                    const lname = studentData.lname;
                    const rollNumber = studentData['Roll Number'];
                    var trow = document.createElement('tr');
                    var td1 = document.createElement('td');
                    var td2 = document.createElement('td');
                    var td3 = document.createElement('td');
                    td1.innerHTML = ++stdNo;
                    td2.innerHTML = rollNumber;
                    td3.innerHTML = fname.concat(" ").concat(lname);
                    trow.appendChild(td1);
                    trow.appendChild(td2);
                    trow.appendChild(td3);
        
                    const attendanceSheet = studentData['Attendance Sheet'];
                    if (attendanceSheet) {
                        fDate.forEach((date) => {
                            if (attendanceSheet.hasOwnProperty(date)) {
                                const lectures = attendanceSheet[date];
                                Object.keys(lectures).forEach((lecture) => {
                                    const attendanceStatus = lectures[lecture];
                                    var td4 = document.createElement('td');
                                    td4.innerHTML = attendanceStatus;
                                    trow.appendChild(td4);
                                });
                            } else {
                                var td4 = document.createElement('td');
                                td4.innerHTML = "_";
                                trow.appendChild(td4);
                            }
                        });
                    } else {
                        for (let i = 0; i < fDate.length; i++) {
                            var td4 = document.createElement('td');
                            td4.innerHTML = "ND";
                            trow.appendChild(td4);
                        }
                    }
                    table.appendChild(trow);
                });
            });
        }
        
        function AddItemsToTable(fname,lname,RollNo,Date,lec1,lec2,lec3){
            var table_body1= document.getElementById('table_body1');
            var trow = document.createElement('tr');
            var td1= document.createElement('td');
            var td2= document.createElement('td');
            var td3= document.createElement('td');
            var td4= document.createElement('td');
            var td5= document.createElement('td');
            var td6= document.createElement('td');
            td1.innerHTML=++stdNo;
            td2.innerHTML=RollNo;
            td3.innerHTML=fname + " " + lname;
            td4.innerHTML=lec1;
            td5.innerHTML=lec2;
            td6.innerHTML=lec3;

            trow.appendChild(td1); 
            trow.appendChild(td2); 
            trow.appendChild(td3);
            trow.appendChild(td4);
            trow.appendChild(td5);
            trow.appendChild(td6);
            tbody.appendChild(trow);
        }



        readUserData();
        