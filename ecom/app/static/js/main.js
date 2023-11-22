$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var em = this.parentNode.children[2] 
    console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/plus_cart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data=",data)
            em.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})
$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var em = this.parentNode.children[2] 
    console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/minus_cart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data=",data)
            em.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})
$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var em = this
    console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/remove_cart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data=",data)
            
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            em.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})


