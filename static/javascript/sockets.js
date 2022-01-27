var chatBox=0
var socket = io();
setTimeout(function(e){console.log("uwu MY BALLS IN YOUR JAW")}, 1000);
console.log(socket)
usr=[]

socket.on('connect', function() {
    console.log("kekwwwww")
    kekw=0
    socket.emit('message', {data: socket.id,"zonenow":"passout"});
});

socket.on('new_message',function(data){
    console.log(data)
    inpID=usr.indexOf(data[1])
    messg=data[0]
    $("#"+inpID+"-list").append("<li>Them: "+messg+" </li>")


})
socket.on('partner', function(user){
    console.log("new mate "+ user)
    $("#"+foundChats+"-load").remove()
    $("#"+foundChats+"-chat").css("opacity",1)
    usr[foundChats]=user
    foundChats+=1
    $(document).on('submit','#usr-signup',function(e){
            e.preventDefault();
    })
});


socket.on('disconnect', function() {
    socket.emit('message', {data: socket});
});
console.log(socket.id)
$( "input" ).submit(function( event ) {
    console.log("kekw")
})




//chat searching functions
chats=0
foundChats=0
$("#chat").click(function(){
    try{
                if (chats<3){

        response=$.ajax({
                type:'POST',
                url:'/loadPage',
                data:{//sends data back to python
                    page:"ChatWindow.html",
                    id:chats
                }
               
            })
             response.done(function(data){
                    console.log("random slab " + data)
                    $(".chatWindow").append(data)
                    chats+=1
                    socket.emit("new_partner",{data: socket.id})


            })
                }
                
    } catch (error){
        alert("something when wrong **DO NOT** close the window and contact me on discord Gohost#4055")
        console.log(error)
        
    }

})  

//chat sending functions??
 $("input").keypress(function(e) {
            // Enter pressed?
            if(e.which == 10 || e.which == 13) {
                msg=$(':focus').val()
                console.log(msg)
            }
        });

$(document).ready(() => {
            $('form').on('submit', () => {
                e.preventDefault();

                return false;
            });
});

 $(document).keypress((e) => {
            if (e.which === 13) {
                e.preventDefault();
                if (chats>=1){
                    inpID=$(':focus').attr('id')[0]
                    messg=$(':focus').val()
                    $("#"+inpID+"-list").append("<li>Me: "+messg+" </li>")
                    response=$.ajax({
                        type:'POST',
                        url:'/sendMsg',
                        data:{//sends data back to python
                            message:messg,self:socket.id,room:usr[inpID]
                            
                        }
                       
                    })
                    console.log(inpID)
                }
            }
})