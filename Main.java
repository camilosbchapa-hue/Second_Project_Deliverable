// Ejercicios Documento Word //

//Primer punto//

let a = 5
let b = 3
console.log(`${a + b}`)

// Estructura selectiva //

let age = 20

if (age >= 18){console.log("Es mayor de edad.")
} else  console.log("No eres mayor de edad.")

// Estructura repetitiva //

let num = 0
for (let i = 0; i <=5; i++ ){
    console.log(`numero: ${i}`)}

// Tipo de estructuras  repetitivas //
// While //
let i = 1
while ( i <= 3){
    console.log(i)
    i++ }
// do while //
let o = 1
do {
    console.log(i)
    o++
} while (o <= 3)
// switch //
let opcion = 2 
switch (opcion){
    case 1:
        console.log("opcion 1")
        break
    case 2: 
        console.log("opcion 2")
        break
    default:
        console.log("Opcion no valida")
}

// Ejemplo combinando TODO // 

for (let e =0; e <=5; e++){
    if (e % 2 === 0){
        console.log(`${e} Es par`)
    } else {
        console.log(`${e} Es impar`)}
    }
