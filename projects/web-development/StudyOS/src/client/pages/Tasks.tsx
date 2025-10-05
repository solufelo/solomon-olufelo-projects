import React, { useState, useEffect } from 'react';
import { useAuth } from 'wasp/client/auth';
import { getTasks, createTask, editTask, deleteTask } from 'wasp/client/operations';
import { DashboardLayout } from '../components/DashboardLayout';
import { Card, Button, Input, EmptyState, Spinner, Alert, Badge } from '../components/UIComponents';
import { CheckSquare, Plus, X, Calendar, Trash2 } from 'lucide-react';

interface Task {
  id: number;
  title: string;
  description: string | null;
  dueDate: string;
  completed: boolean;
  createdAt: string;
}

const Tasks: React.FC = () => {
  const { data: user } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [formData, setFormData] = useState({ 
    title: '', 
    description: '', 
    dueDate: new Date().toISOString().split('T')[0] 
  });

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await getTasks();
      setTasks(data);
    } catch (error) {
      console.error('Error loading tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createTask({
        title: formData.title,
        description: formData.description || null,
        dueDate: new Date(formData.dueDate),
      });
      setFormData({ title: '', description: '', dueDate: new Date().toISOString().split('T')[0] });
      setShowCreateForm(false);
      loadTasks();
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  const handleToggleComplete = async (task: Task) => {
    try {
      await editTask({
        id: task.id,
        data: { completed: !task.completed }
      });
      loadTasks();
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleDeleteTask = async (taskId: number) => {
    if (confirm('Are you sure you want to delete this task?')) {
      try {
        await deleteTask({ id: taskId });
        loadTasks();
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    }
  };

  const pendingTasks = tasks.filter(t => !t.completed);
  const completedTasks = tasks.filter(t => t.completed);

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between animate-fade-in">
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">Tasks</h1>
            <p className="text-muted-foreground">Manage your study tasks and deadlines</p>
          </div>
          <Button 
            onClick={() => setShowCreateForm(!showCreateForm)}
            size="lg"
          >
            {showCreateForm ? <><X className="w-5 h-5" />Cancel</> : <><Plus className="w-5 h-5" />New Task</>}
          </Button>
        </div>

        {/* Create Task Form */}
        {showCreateForm && (
          <Card className="animate-card-rise">
            <form onSubmit={handleCreateTask} className="space-y-4">
              <Input
                label="Task Title"
                placeholder="e.g., Study for Math Exam"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                autoFocus
                required
              />
              <div>
                <label className="text-sm font-medium text-foreground block mb-2">Description</label>
                <textarea
                  className="form-input min-h-[80px]"
                  placeholder="Optional description..."
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                />
              </div>
              <Input
                label="Due Date"
                type="date"
                value={formData.dueDate}
                onChange={(e) => setFormData({ ...formData, dueDate: e.target.value })}
                required
              />
              <div className="flex gap-3">
                <Button type="submit">Create Task</Button>
                <Button 
                  type="button" 
                  variant="outline"
                  onClick={() => {
                    setShowCreateForm(false);
                    setFormData({ title: '', description: '', dueDate: new Date().toISOString().split('T')[0] });
                  }}
                >
                  Cancel
                </Button>
              </div>
            </form>
          </Card>
        )}

        {/* Tasks List */}
        {loading ? (
          <div className="flex justify-center py-12">
            <Spinner size="lg" />
          </div>
        ) : tasks.length === 0 ? (
          <EmptyState
            icon={<CheckSquare className="w-12 h-12" />}
            title="No tasks yet"
            description="Create your first task to start organizing your study schedule."
            action={{
              label: 'Create Your First Task',
              onClick: () => setShowCreateForm(true)
            }}
          />
        ) : (
          <div className="space-y-6">
            {/* Pending Tasks */}
            {pendingTasks.length > 0 && (
              <div>
                <h2 className="text-xl font-semibold text-foreground mb-4">
                  Pending ({pendingTasks.length})
                </h2>
                <div className="space-y-3">
                  {pendingTasks.map((task) => (
                    <Card key={task.id} className="hover-lift">
                      <div className="flex items-start gap-4">
                        <button
                          onClick={() => handleToggleComplete(task)}
                          className="mt-1 w-5 h-5 rounded border-2 border-muted-foreground hover:border-primary transition-colors flex items-center justify-center"
                        >
                          {task.completed && <CheckSquare className="w-4 h-4 text-primary" />}
                        </button>
                        <div className="flex-1 min-w-0">
                          <h3 className="font-semibold text-foreground mb-1">{task.title}</h3>
                          {task.description && (
                            <p className="text-sm text-muted-foreground mb-2">{task.description}</p>
                          )}
                          <div className="flex items-center gap-2 text-sm text-muted-foreground">
                            <Calendar className="w-4 h-4" />
                            <span>{new Date(task.dueDate).toLocaleDateString()}</span>
                          </div>
                        </div>
                        <button
                          onClick={() => handleDeleteTask(task.id)}
                          className="p-2 text-muted-foreground hover:text-destructive hover:bg-destructive/10 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </Card>
                  ))}
                </div>
              </div>
            )}

            {/* Completed Tasks */}
            {completedTasks.length > 0 && (
              <div>
                <h2 className="text-xl font-semibold text-foreground mb-4">
                  Completed ({completedTasks.length})
                </h2>
                <div className="space-y-3">
                  {completedTasks.map((task) => (
                    <Card key={task.id} className="opacity-60 hover:opacity-100 transition-opacity">
                      <div className="flex items-start gap-4">
                        <button
                          onClick={() => handleToggleComplete(task)}
                          className="mt-1 w-5 h-5 rounded border-2 border-success bg-success flex items-center justify-center"
                        >
                          <CheckSquare className="w-4 h-4 text-white" />
                        </button>
                        <div className="flex-1 min-w-0">
                          <h3 className="font-semibold text-foreground mb-1 line-through">{task.title}</h3>
                          {task.description && (
                            <p className="text-sm text-muted-foreground mb-2">{task.description}</p>
                          )}
                          <div className="flex items-center gap-2 text-sm text-muted-foreground">
                            <Calendar className="w-4 h-4" />
                            <span>{new Date(task.dueDate).toLocaleDateString()}</span>
                          </div>
                        </div>
                        <button
                          onClick={() => handleDeleteTask(task.id)}
                          className="p-2 text-muted-foreground hover:text-destructive hover:bg-destructive/10 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </Card>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </DashboardLayout>
  );
};

export default Tasks;
export { Tasks };
