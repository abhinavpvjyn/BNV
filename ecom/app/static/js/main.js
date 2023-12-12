$('.add-cart').click(function(){
    var id = $(this).attr("pid").toString();
    // var em = this.parentNode.children[2] 
    console.log("pid=",id)
    $.ajax({
        type:"GET",
        url:"/add_cart",
        data:{
            prod_id:id
        },
        // success:function(data){
        //     console.log(data.max)
        //     document.getElementById("addcart").innerText=data.max
            
        // }
    })
})
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
        success:function(data1){
            console.log("data=",data1)
            
            document.getElementById("amount").innerText=data1.amount
            document.getElementById("totalamount").innerText=data1.totalamount
            em.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})
$('.delete-address').click(function(){
    console.log('clicked delete')
    var id=$(this).attr("aid").toString();
    console.log(id)
})


$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{prod_id:id},
        success:function(data){
            window.location.reload()
        }
        
    })
})

$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{prod_id:id},
        success:function(data){
            window.location.reload()
        }
        
    })
})

$('.delete-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/deletewishlist",
        data:{prod_id:id},
        success:function(data){
            window.location.reload()
        }
        
    })
})



