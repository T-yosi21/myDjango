
btn_
let elements4 = payjp.elements()

// 入力フォームを分解して管理・配置できます
let numberElement = elements4.create('cardNumber')
let expiryElement = elements4.create('cardExpiry')
let cvcElement = elements4.create('cardCvc')
numberElement.mount('#number-form')
expiryElement.mount('#expiry-form')
cvcElement.mount('#cvc-form')

// createTokenの引数には任意のElement1つを渡します
function onSubmit2(event) {
  payjp.createToken(numberElement).then(function(r) {
    document.querySelector('#token2').innerText = r.error ? r.error.message : r.id
  })
}