/*
Combining components together
The most fundamental and useful part of React is that
you can create any number of components and nest them
just like you would any HTML tag. You pass down data
to your components from parent components in a one-way
data flow.
Note: If you use something like Flux/Reflux you have a bit
power when it comes to data storage and event handling.
Using a Flux-like framework with React is very helpful.
*/

var ProductItem = React.createClass({
  render: function () {
    return (
      <tr>
        <td>{this.props.name}</td>
        <td>{this.props.price}</td>
      </tr>
    );
  }
});

var ProductList = React.createClass({
  render: function () {
    var products = this.props.products.map(function (product, index) {
      return (
        <ProductItem
          key={index}
          name={product.name}
          price={product.price}
        />
      );
    });

    return (
      <table>
        {products}
      </table>
    );
  }
});

// Could come from an API, LocalStorage, another component, etc...
var products = [
  { name: 'Toast', price: 1499 },
  { name: 'Bacon', price: 3245 },
  { name: 'Coffee', price: 300 }
];

ReactDOM.render(<ProductList products={products} />, document.getElementById('root'));
