function addToCart(n){
    axios.post('dumbbells',{
        item: n
    }).then((response)=>{
        window.location.href='/cart'
    })
}