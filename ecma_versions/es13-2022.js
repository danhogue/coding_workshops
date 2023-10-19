// EMCAScript 2022 - ES2022 - ES13

// Top level await and dynamic import
// Notes:
//  Export in i18n.en.js and top level await need "type": "module" setting
//  in package.js to work
await Promise.resolve(console.log("Hello"));
{
  const navigator = { language: 'en' }
  const { i18n } = await import(`./i18n/${navigator.language}.js`);
  await Promise.resolve(console.log(i18n.hello));
}

// Private instance fields and methods
(function(){
  class PrivateClass {
    #nope = 'not happening'
    #alsoNo = function () {
      return 'uhuh';
    }
    ok = 'lol'
    yes = function () {
      return this.ok;
    }
  }
  const pc = new PrivateClass();
  // console.log(pc.nope)
  // console.log(pc.alsoNo)
  // console.log(pc.ok)
  // console.log(pc.yes())
})();

// Static class field, methods, and init blocks
(function(){
class StatClass {
  static a = 1;
  static b;
  static foo = function () { return this.b }
  static {
    this.b = 2;
  }
}
// console.log(StatClass.b);
// console.log(StatClass.foo());
})();

// Error .cause()
(async function(){
  const getUsers = async(array) => {
    const users = await fetch("https://ajsdkflsa.jfdksal");
    console.log(array)
    return users;
  }

  try {
    const users = await getUsers(['foo']);
    console.log("bar")
  } catch (err) {
    // console.log(err)
    // console.log(err.cause)
  }
})();

// Array .at()
(function(){
const arr = [1,'cool',3];
// console.log(arr.at(1))
// console.log(arr.at(-2))
})();

// Object .hasOwn()
(function(){
  const bar = {}
  // console.log(Object.hasOwn(bar, 'foo'))
  const foo = { bar: 1 }
  // console.log(Object.hasOwn(foo, 'bar'))
})();

// Regex match .indices ('d' flag)
(function(){
  const result = [..."hello1hello2hello3".matchAll(/[a-z]+([1,4])/dg)];
  // console.log(result);
  // console.log(result[0].indices)
})();
