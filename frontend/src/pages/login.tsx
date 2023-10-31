import z from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

const Schema = z.object({
  email: z.string().email().min(2),
  password: z.string().min(2),
});

type FormData = z.infer<typeof Schema>;

const Login = () => {
  const onSubmit = () => {
    event.preventDefault();
    console.log("submit");
  };

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>();

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-[250px]">
        <form onSubmit={onSubmit}>
          <div className="grid gap-4">
            <div className="grid gap-1">
              <label>Email</label>
              <input
                placeholder="name@example.com"
                type="email"
                autoCapitalize="none"
                autoComplete="email"
                autoCorrect="off"
                className="py-1 px-2 rounded border-2 border-black"
              />
            </div>
            <div className="grid gap-1">
              <label>Password</label>
              <input
                placeholder="*****"
                type="password"
                autoCapitalize="none"
                autoCorrect="off"
                className="py-1 px-2 rounded border-2 border-black"
              />
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
