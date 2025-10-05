import { create } from "zustand"

interface User {
  _id: string
  name: string
  email: string
  isAdmin: boolean
  isActive: boolean
}

interface UserStore {
  currentUser: User | null
  setCurrentUser: (user: User | null) => void
  clearUser: () => void
}

const userStore = create<UserStore>((set) => ({
  currentUser: null,
  setCurrentUser: (user) => set({ currentUser: user }),
  clearUser: () => set({ currentUser: null })
}))

export default userStore