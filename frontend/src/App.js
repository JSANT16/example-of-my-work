import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import "./App.css"
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.min.css';
import NotFound from './pages/NotFound';
import Header from './components/Header';
import Home from './pages/Home';
import Custumers from './pages/Custumers';
import Articles from './pages/Articles'
import Orders from './pages/Orders'
import Vendors from './pages/Vendors';

const App = () => {
  return (
    <>
      <Router>
        <Header />
        <br />
        <Container>
          <Switch>
            <Route exact path='/' component={Home} />
            <Route exact path='/articles' component={Articles} />
            <Route exact path='/orders' component={Orders} />
            <Route exact path='/custumers' component={Custumers} />
            <Route exact path='/vendors' component={Vendors} />
            <Route exact path='*' component={NotFound} />
          </Switch>
        </Container>

      </Router>
    </>
  )
}

export default App;
