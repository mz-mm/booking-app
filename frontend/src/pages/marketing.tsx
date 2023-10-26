import { Link } from "react-router-dom";

const Marketing = () => {
  return (
    <main>
      <header className="flex justify-between items-center fixed top-0 left-0 right-0 m-2 p-2">
        <Link to={"/"}>Booking</Link>
        <nav className="space-x-2">
          <Link className="bg-blue-500 p-2 rounded" to={"/signup"}>
            Sign up
          </Link>
          <Link
            className="bg-zinc-500 hover:bg-zinc-600 p-2 rounded"
            to={"/login"}
          >
            Login in
          </Link>
        </nav>
      </header>
    </main>
  );
};

export default Marketing;
