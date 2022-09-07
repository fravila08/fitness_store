function addToCart(n){
    axios.post('fitness',{
        item: n
    }).then(
        window.location.href='/cart'
    )
}