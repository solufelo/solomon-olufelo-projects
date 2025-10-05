import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { max } from 'three/tsl';

// initialize the scene
const scene = new THREE.Scene()

// initialize the renderer
const canvas = document.querySelector('canvas.threejs')
const renderer = new THREE.WebGLRenderer({
  canvas: canvas
})
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

// add objects to the scene
const cubeGeometry = new THREE.BoxGeometry(1,1,1)
const cubeMaterial = new THREE.MeshBasicMaterial({color: "red", wireframe: true})

const cubeMesh = new THREE.Mesh(
  cubeGeometry,
  cubeMaterial
)
scene.add(cubeMesh)
const axesHelper = new THREE.AxesHelper(10)
// scene.add(axesHelper)

cubeMesh.position.x = 0
cubeMesh.position.y = 0
cubeMesh.position.z = 0

// initialize the camera
const camera = new THREE.OrthographicCamera(
  -1 * (window.innerWidth / window.innerHeight),
  1 * (window.innerWidth / window.innerHeight),
  1,
  -1,
  0.1,
  100
)
camera.position.z = 5

// Handle window resize
const handleResize = () => {
  const aspectRatio = window.innerWidth / window.innerHeight
  camera.left = -1 * aspectRatio
  camera.right = 1 * aspectRatio
  camera.top = 1
  camera.bottom = -1
  camera.updateProjectionMatrix()
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener('resize', handleResize)

//initialize the orbit controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true
controls.autoRotate = true

//renderloop
const renderloop = () => {
  controls.update()
  renderer.render(scene, camera)
  window.requestAnimationFrame(renderloop)
}

renderloop()