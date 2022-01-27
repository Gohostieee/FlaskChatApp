	function loadPage(reqs,reqPage){

			response=$.ajax({
		        type:'POST',
		        url:'/loadPage',
		        data:{//sends data back to python
		         	page:reqs
		        }
		       
		    })
		     response.done(function(data){
		     	console.log("random slab " + data)
		    	window.deets=data
		    	console.log("do it w 2 " + window.deets)
		   		$(reqPage).html(window.deets)
		   		setTimeout(function() {
		    			loadingScreenDown()
					}, 1000);
		    })

		}
