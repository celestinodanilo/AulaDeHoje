import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Guilds } from "./guild";
import { Members } from "./member";
import { GuildForm } from "./guildForm";
import { MemberForm } from "./memberForm";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Guilds />} />
        <Route path="/guilds/:guildId" element={<GuildForm />} />
        <Route path="/members" element={<Members />} />
        <Route path="/members/:memberId" element={<MemberForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;