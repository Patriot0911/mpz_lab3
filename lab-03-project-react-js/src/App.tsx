import './App.css'

const homeVideo = 'https://cutt.ly/Kw4Tl5GF';

const App = () => {
  const clickHandle = () => {
    window.open(homeVideo, '_blank')
  };
  // comment
  return (
    <main>
      <section
        onClick={clickHandle}
      >
        Hello world!
      </section>
    </main>
  );
};

export default App
