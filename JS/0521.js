// Array Helper Methods

// case 1.
// ES5
var colors = ['red','blue','green']

// for (var i = 1; i<colors.length; i++) {
//     console.log(colors[i]);
// } => ES6이상에서는 forEach로 대체가능

// colors의 배열의 원소를 함수에 할당해서 해당작업을 수행
// => 익명함수를 사용하면 일반적인 for 문처럼 사용가능
colors.forEach(function(color){
    console.log(color)
})

// case 2.
// ES5
var numbers = [1,2,3,]
// for 문
// var doubleNumbers = []
// for (var i = 0; i< numbers.length; i++) {
//     doubleNumbers.push(numbers[i]*2)
// } 

// ES6이상 map, filter 존재
const doubleNumbers = numbers.map(function(number){
    return number * 2
}) // 리턴값으로 새로운 배열을 만듬
console.log(doubleNumbers)

const products = [
    {name : 'cucumber', type : 'vegetable'},
    {name : 'banana', type : 'vegetable'},
    {name : 'carrot', type : 'fruit'},
    {name : 'apple', type : 'fruit'},
]

const fruitProducts = products.filter(function(product){
    return product.type === 'fruit'
}) // 조건이 true인 경우에만 객체를 가져와 새로운 배열에 넣어줌
console.log(fruitProducts)

// ES6 이상 find method 존재

const users = [
    {name : 'nwith'},
    {name : 'admin'},
    {name : 'zzuli'},
    {name : 'admin'},
]
const foundUser = users.find(function(user){
    return user.name === 'admin'
}) // 하나만 찾는다. 적은 인덱스 우선
console.log(foundUser)

// ES6 이상 every&some 
const computers = [
    {name:'macbook', ram : 16 },
    {name:'gram', ram : 8 },
    {name:'series9', ram : 32 },    
]
const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16
})

const someComputersAvailable = computers.some(function(computer){
    return computer.ram > 16
})
console.log(everyComputersAvailable)
console.log(someComputersAvailable)
// false
// true
