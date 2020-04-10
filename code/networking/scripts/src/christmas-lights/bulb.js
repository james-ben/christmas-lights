'use strict';

class Bulb extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
      <li></li>
    );
  }
}

const domContainer = document.querySelector('li');
ReactDOM.render(React.createElement(Bulb), domContainer);