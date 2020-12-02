# forEach

对数组中的每个元素进行操作，无法使用`break`和`return`

```javascript
var arr = [1, 2, 3]
arr.forEach(elem => {
  console.log(elem)
})
```

# for-in

`for-in`适合用来循环`enemurable`对象。

```javascript
var obj = {'a': 1, 'b': 2, 'c': 3}
for (const key in obj) {
  // key: string
  console.log(key + obj[key])
}
```

# for-of

`for-of`循环是对`for-in`循环的改进，补齐了`forEach`和`for-in`的短板。
可以作用于多个对象。

+ string, array

+ enemurable

```javascript
var obj = { 'a': 1, 'b': 2, 'c': 3 }
for (const key in Object.keys(obj)) {
  console.log(key + ' ' + obj[key])
}
```

+ Map

```javascript
var map = new Map([['a', 1], ['b', 2], ['c', 3]])
for (const [key, value] of map) {
  console.log(key + ' ' + value)
}
```

+ Set

```javascript
let iterable = new Set([1, 1, 2, 2, 3, 3]);
for (let value of iterable) {
  console.log(value);
}
```

+ DOM

```javascript
let articleParagraphs = document.querySelectorAll("article > p");
for (let paragraph of articleParagraphs) {
  paragraph.classList.add("read");
}
```

+ generator
