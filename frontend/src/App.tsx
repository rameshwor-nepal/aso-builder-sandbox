
import './App.css'
import { Button } from './components/ui/button'

function App() {

  return (
    <>
      <section id="center">
        <h1 className="text-3xl font-bold underline">
          Hello world!
        </h1>
        <div className="flex min-h-screen items-center justify-center">
          <Button>Click me</Button>
        </div>
      </section>
    </>
  )
}

export default App
