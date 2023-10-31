import {Route, Routes} from "react-router-dom";
import Marketing from "./pages/marketing.tsx";
import Login from "./pages/login.tsx";
import Signup from "./pages/signup.tsx";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Marketing />} />
          <Route path="/login" element={<Login />}/>
          <Route path="/signup" element={<Signup />}/>
      </Routes>
  )
}

export default App
