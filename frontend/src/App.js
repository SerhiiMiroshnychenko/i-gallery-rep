import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Search from './components/Search';

const App = () => {
  return (
    <div className="App">
      <Header title="I-gallery" />
      <Search />
    </div>
  );
}

export default App;
