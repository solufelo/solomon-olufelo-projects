# Quick Reference Guide

## 🚀 Essential Commands

### Development Setup
```bash
# Start both servers
Terminal 1: cd server && npm start
Terminal 2: cd client && npm run dev

# Kill processes if needed
pkill -f vite
pkill -f "node.*index.js"

# Clear caches
cd client && rm -rf node_modules/.vite
```

### Testing APIs
```bash
# Test server connection
curl http://localhost:5000/

# Get all users
curl http://localhost:5000/api/users/

# Register test user
curl -X POST http://localhost:5000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"password123"}'

# Login test user
curl -X POST http://localhost:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

---

## 📁 File Structure Quick Reference

```
client/src/
├── components/         # Reusable UI components
├── pages/             # Main page components
│   ├── auth/          # Login, Register, Dashboard
│   ├── campaigns/     # Campaign management
│   ├── donations/     # Donation tracking
│   ├── profile/       # User profile
│   ├── reports/       # Analytics
│   ├── settings/      # User settings
│   └── users/         # Admin user management
├── layout/            # Header, layouts
├── store/             # Zustand state management
├── interfaces/        # TypeScript interfaces
└── providers/         # Theme, context providers

server/
├── config/            # Database configuration
├── models/            # Mongoose schemas
├── routes/            # API endpoints
└── middleware/        # Custom middleware
```

---

## 🔧 Common Code Patterns

### New Page Component Template
```typescript
import { Typography, Card } from 'antd'
import { SomeIcon } from '@ant-design/icons'

const { Title, Text } = Typography

function NewPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <Title level={1} className="flex items-center gap-3">
          <SomeIcon />
          Page Title
        </Title>
        <Text type="secondary">Page description</Text>
      </div>
      
      <Card>
        {/* Page content */}
      </Card>
    </div>
  )
}

export default NewPage
```

### API Route Template
```javascript
router.get('/endpoint', async (req, res) => {
  try {
    // Your logic here
    res.status(200).json({ message: 'Success', data: result })
  } catch (error) {
    res.status(500).json({ message: 'Operation failed', error })
  }
})
```

### State Management (Zustand)
```typescript
import { create } from "zustand"

interface StoreState {
  data: any[]
  setData: (data: any[]) => void
  clearData: () => void
}

const useStore = create<StoreState>((set) => ({
  data: [],
  setData: (data) => set({ data }),
  clearData: () => set({ data: [] })
}))

export default useStore
```

---

## 🎨 UI Component Patterns

### Form with Validation
```typescript
<Form layout="vertical" onFinish={onFinish}>
  <Form.Item
    name="fieldName"
    label="Field Label"
    rules={[{ required: true, message: 'Please enter field' }]}
  >
    <Input placeholder="Enter value" />
  </Form.Item>
  <Form.Item>
    <Button type="primary" htmlType="submit" loading={loading}>
      Submit
    </Button>
  </Form.Item>
</Form>
```

### Data Table
```typescript
const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Actions',
    key: 'actions',
    render: (record) => (
      <Button onClick={() => handleAction(record)}>
        Action
      </Button>
    ),
  },
]

<Table 
  columns={columns} 
  dataSource={data} 
  rowKey="id"
  pagination={{ pageSize: 10 }}
/>
```

### Statistics Cards
```typescript
<Row gutter={[16, 16]}>
  <Col xs={24} sm={8}>
    <Card>
      <Statistic
        title="Total"
        value={1234}
        prefix="$"
        valueStyle={{ color: '#3f8600' }}
      />
    </Card>
  </Col>
</Row>
```

---

## 🔐 Authentication Patterns

### Protected Route Check
```typescript
const token = Cookies.get('token') || localStorage.getItem('token')
if (!token) {
  navigate('/login')
  message.error('Please login to continue')
  return
}
```

### API Request with Auth
```typescript
const token = localStorage.getItem('token')
const response = await axios.get('/api/endpoint', {
  headers: {
    Authorization: `Bearer ${token}`
  }
})
```

### Role-Based Access
```typescript
// In component
const { currentUser } = userStore()
if (!currentUser?.isAdmin) {
  return <div>Access Denied</div>
}

// In navigation
if (currentUser?.isAdmin) {
  menuItems.push({
    key: 'admin',
    label: 'Admin Panel',
    // ...
  })
}
```

---

## 🗄️ Database Patterns

### Mongoose Model Template
```javascript
import mongoose from 'mongoose'

const schema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
})

export default mongoose.model('ModelName', schema)
```

### CRUD Operations
```javascript
// Create
const item = await Model.create(data)

// Read
const items = await Model.find()
const item = await Model.findById(id)

// Update
const updated = await Model.findByIdAndUpdate(id, data, { new: true })

// Delete
const deleted = await Model.findByIdAndDelete(id)
```

---

## 🚨 Error Handling Patterns

### Frontend Error Handling
```typescript
try {
  setLoading(true)
  const response = await axios.post('/api/endpoint', data)
  message.success('Operation successful')
  // Handle success
} catch (error: any) {
  const errorMessage = error?.response?.data?.message || 'Operation failed'
  message.error(errorMessage)
  console.error('Error:', error)
} finally {
  setLoading(false)
}
```

### Backend Error Handling
```javascript
try {
  // Database operation
  const result = await Model.findById(id)
  if (!result) {
    return res.status(404).json({ message: 'Not found' })
  }
  res.json({ message: 'Success', data: result })
} catch (error) {
  console.error('Error:', error)
  res.status(500).json({ 
    message: 'Internal server error',
    error: process.env.NODE_ENV === 'development' ? error.message : {}
  })
}
```

---

## 🔍 Debugging Tips

### Common Issues & Solutions

**Issue**: Infinite re-renders
```typescript
// ❌ Wrong - causes infinite loop
useEffect(() => {
  setData(newData)
}, [data])

// ✅ Correct - specify dependencies
useEffect(() => {
  setData(newData)
}, [someSpecificDependency])
```

**Issue**: CORS errors
```javascript
// Add to server
app.use(cors({
  origin: "http://localhost:5173",
  credentials: true
}))
```

**Issue**: Token not found
```typescript
// Check both storage locations
const token = Cookies.get('token') || localStorage.getItem('token')
```

### Browser DevTools
- **Console**: Check for errors and warnings
- **Network**: Monitor API requests and responses  
- **Application**: Check localStorage and cookies
- **Components**: Use React DevTools for state inspection

---

## 📝 Git Workflow

### Branch Naming
- `feature/user-authentication`
- `bugfix/login-redirect-issue`
- `hotfix/security-vulnerability`

### Commit Messages
```bash
git commit -m "feat: add user profile page"
git commit -m "fix: resolve infinite loop in auth"
git commit -m "docs: update API documentation"
```

### Common Git Commands
```bash
# Create and switch to new branch
git checkout -b feature/new-feature

# Add and commit changes
git add .
git commit -m "feat: implement new feature"

# Push to remote
git push origin feature/new-feature

# Merge to main
git checkout main
git merge feature/new-feature
```

---

## 🔧 Environment Variables

### Server (.env)
```env
MONGODB_URL=mongodb+srv://user:pass@cluster.mongodb.net/db
JWT_SECRET=your-super-secret-jwt-key
PORT=5000
NODE_ENV=development
```

### Client (if needed)
```env
VITE_API_URL=http://localhost:5000
VITE_APP_NAME=CAPTAIN-FUNDS
```

---

**Quick Links**:
- [Main README](../README.md)
- [AI Development Rules](./AI-DEVELOPMENT-RULES.md)
- [Development Progress](./DEVELOPMENT-PROGRESS.md)

**Last Updated**: September 10, 2024
