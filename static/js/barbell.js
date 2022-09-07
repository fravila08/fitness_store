function addToCart(n){
    axios.post('barbells',{
        item: n
    }).then((response)=>{
        window.location.href='/cart'
    })
}