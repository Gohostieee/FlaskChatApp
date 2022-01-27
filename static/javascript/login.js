auth=null
		$(document).on('submit','#usr-signup',function(e){
      		e.preventDefault();
      		if (auth=="sign-up"){
	      		req=$.ajax({
			        type:'POST',
			        url:'/login',
			        data:{//sends data back to python
			         	username:$("#nameBox").val(),
			         	password:$("#passBox").val(),
			         	request:"sign-up"
			        }
			       
			    })
	      		req.done(function(data) {
		      				console.log(data.message)
							if (data.status!="authorized"){
								$("#screener").toggleClass('visible').removeClass('hidden');
							}

							switch(data.status){
								case("err-001"):
									console.log("user already exists")
									$("#error").text("user already exists")
								break;
								case("err-002"):
									var msg = "password must have "
									var errKeys = Object.keys(data.message) 
									console.log(errKeys)
									for (let i = 0; i < errKeys.length;i++){
											if (i == errKeys.length-1 && errKeys.length !=1){
													msg = msg.concat(' and ',data.message[i])

											}else{
													msg = msg.concat(' ',data.message[i], ',')
											}
											console.log(data.message[i])
									}
									console.log(msg)
									$("#error").text(msg)
								break;
								case("authorized"):
			    					loadPage("charCreate.html","#mainContainer")
		    						setTimeout(function() {
		  					  			loadingScreenDown()
									}, 1000);
									localStorage.setItem("userAuth",data.message)
								break;
								
							}
				});
	      	}
	      	else{
	      		req=$.ajax({
			        type:'POST',
			        url:'/login',
			        data:{//sends data back to python
			         	username:$("#nameBox").val(),
			         	password:$("#passBox").val(),
			         	request:"login"
			        }
			       
			    })
			    req.done(function(data){
			    	console.log(data)
			    	switch(data.status){
			    		case "authorized":
			    			loadPage("charCreate.html","#mainContainer")
		    				setTimeout(function() {
		    					loadingScreenDown()
							}, 1000);
							localStorage.setItem("userAuth",data.message)

			    		break;
			    	}
			    })
	      	}
      	})

//check if users are already logged in
//CONSIDER CHANGING THIS INTO A HASH SINCE IT HAS SOME PROS AND SOME CONS
	console.log(localStorage.getItem("userAuth"))
		function userCheck(){
			console.log(localStorage.getItem("userAuth"))
			kekw=localStorage.getItem('userAuth')
			if  (kekw==null){
				setTimeout(function() {
		    		loadingScreenDown()
				}, 1000);
				return "uwu"
			}
			response=$.ajax({
		        type:'POST',
		        url:'/generalFunctions',
		        data:{//sends data back to python
		         	req:"checkUser",
		         	user:localStorage.getItem("userAuth")
		        }
		       
		    })
		    response.done(function(data){
		    	if ("authorized" == data){
			    	loadPage("charCreate.html","#mainContainer")
		    		console.log(window.deets+ " we need to die rn cuz")
		    		
		    	}

		    })

		}

		userCheck()
