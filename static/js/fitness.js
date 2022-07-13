function addToCart(n){
    axios.post('fitness',{
        item: n
    }).then((response)=>{
        window.location.href='fitness'
    })
}