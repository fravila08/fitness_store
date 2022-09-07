function remove(n){
    axios.post('cart',{
    item: n
}).then((response)=>{
    window.location.href='/cart'
})
}