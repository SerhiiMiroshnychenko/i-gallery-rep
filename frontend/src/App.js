import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Search from './components/Search';

const handleSearchSubmit = (e) => {
  e.preventDefault();
  console.log (e.target[0].value);
}

const App = () => {
  return (
    <div className="App">
      <Header title="Ї-gallery" />
      <Search handleSubmit={handleSearchSubmit} />
    </div>
  );
}

export default App;
